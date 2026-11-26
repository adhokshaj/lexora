#!/usr/bin/env python3
"""Build a local Princeton WordNet 3.0 dictionary; standard library only."""
import collections, io, json, pathlib, re, sys, urllib.request, zipfile
ROOT=pathlib.Path(__file__).resolve().parent
URL='https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip'
def build(raw):
    z=zipfile.ZipFile(io.BytesIO(raw)); files={pathlib.PurePosixPath(n).name:n for n in z.namelist() if not n.endswith('/')}
    def read(n):return z.read(files[n]).decode('utf-8')
    syn={}; order={}; aliases={}; tags={}; groups=collections.defaultdict(set)
    posnames={'n':'noun','v':'verb','a':'adjective','s':'adjective','r':'adverb'}
    for suffix in ('noun','verb','adj','adv'):
        for line in read('index.'+suffix).splitlines():
            if not line or line.startswith(' '):continue
            p=line.split(); count=int(p[3]); offsets=p[6+count:]; order[(p[0].replace('_',' ').lower(),p[1])]=offsets
            tags[(p[0].replace('_',' ').lower(),p[1])]=int(p[5+count])
        for line in read('data.'+suffix).splitlines():
            if not line or not line[0].isdigit():continue
            left,gloss=line.split('|',1); p=left.split(); off,lex,pos=p[:3]; pos='a' if pos=='s' else pos; n=int(p[3],16); words=[p[4+i*2].replace('_',' ').lower() for i in range(n)]; k=4+2*n; pc=int(p[k]); pointers=[p[k+1+i*4:k+5+i*4] for i in range(pc)]; examples=re.findall(r'"([^"]+)"',gloss); definition=re.sub(r'\s*;?\s*"[^"]+"','',gloss).strip(' ;'); syn[(pos,off)]=(words,definition,examples,pointers,lex)
        if suffix+'.exc' in files:
            for line in read(suffix+'.exc').splitlines():
                a,*b=line.split();aliases.setdefault(a.replace('_',' '),[]).extend(x.replace('_',' ') for x in b)
    out={}
    for (word,pos),offsets in order.items():
        entry=out.setdefault(word,{'senses':[],'frequency':0}); entry['frequency']+=tags[(word,pos)]
        for off in offsets:
            if (pos,off) not in syn:continue
            words,d,ex,ptr,lex=syn[(pos,off)]; ant=[]
            for symbol,target,tpos,indices in ptr:
                if symbol!='!' or len(indices)!=4:continue
                src,dst=int(indices[:2],16),int(indices[2:],16); other=syn.get(('a' if tpos=='s' else tpos,target))
                if other and src and src<=len(words) and words[src-1]==word and dst and dst<=len(other[0]):ant.append(other[0][dst-1])
            if d:entry['senses'].append({'p':posnames[pos],'d':d,'e':ex,'s':list(dict.fromkeys(x for x in words if x!=word)),'a':list(dict.fromkeys(ant))});groups[lex].add(word)
    out={w:e for w,e in out.items() if e['senses']}
    for w,e in out.items():
        f=e.pop('frequency'); first=e['senses'][0]; e.update(d=first['d'],e='; '.join(first['e']),s=', '.join(first['s']),a=', '.join(first['a']),level=1 if f>=8 and len(w)<=8 else 2 if f>=3 else 3 if f>=1 else 4,study=f>=1 and w.isalpha())
    aliases={w:list(dict.fromkeys(x for x in xs if x in out)) for w,xs in aliases.items() if w not in out}; aliases={w:x for w,x in aliases.items() if x}
    lexnames={}
    if 'lexnames' in files:
        for l in read('lexnames').splitlines():
            p=l.split(); lexnames[p[0]]=p[1]
    lists={}
    for lex,words in groups.items():
        name=lexnames.get(lex,lex).replace('noun.','Nouns: ').replace('verb.','Verbs: ').replace('adj.','Adjectives: ').replace('adv.','Adverbs: ').replace('_',' ').replace('noun.','').capitalize()
        pool=sorted((w for w in words if out[w]['study']),key=lambda w:(out[w]['level'],w))
        for tier,levels in [('Core',(1,2)),('Advanced',(3,4))]:
            selected=[w for w in pool if out[w]['level'] in levels][:120]
            if len(selected)>=5:lists[name+' · '+tier]=selected
    assert len(out)>100000, f'Unexpected dictionary size: {len(out)}'
    for w in ('run','bank','stoic','irreverent','callous','pragmatic'):assert w in out,w
    assert len(out['run']['senses'])>10
    license=read('LICENSE'); (ROOT/'WORDNET-LICENSE.txt').write_text(license)
    payload='const fullDictionary='+json.dumps(out,ensure_ascii=True,separators=(',',':'))+';\nconst inflections='+json.dumps(aliases,separators=(',',':'))+';\nconst lexicalCollections='+json.dumps(lists,separators=(',',':'))+';\n'
    temp=ROOT/'dictionary.tmp';temp.write_text(payload);temp.replace(ROOT/'dictionary.js');print(f'Built {len(out):,} headwords, {sum(len(e["senses"]) for e in out.values()):,} senses, {len(lists)} lexical collections.')
if __name__=='__main__':
    raw=pathlib.Path(sys.argv[1]).read_bytes() if len(sys.argv)>1 else urllib.request.urlopen(URL,timeout=120).read();build(raw)
