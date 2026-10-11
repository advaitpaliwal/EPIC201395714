import os, urllib.parse, subprocess, json, math, datetime
D=os.path.expanduser('~/Scratch/EPIC201395714-work/recheck_2026-10-11')
ra,dec=183.90161,-1.02649; q=urllib.parse.quote
def get(name,url):
    p=os.path.join(D,name); open(p+'.url','w').write(url+'\nfetched '+datetime.datetime.utcnow().isoformat()+'Z\n')
    r=subprocess.run(['curl','-sL','--max-time','180','-o',p,url]); print(name,r.returncode,os.path.getsize(p) if os.path.exists(p) else -1,flush=True)
c=abs(math.cos(math.radians(dec)))
box=f"ra between {ra-2/60/c} and {ra+2/60/c} and dec between {dec-2/60} and {dec+2/60}"
nea="https://exoplanetarchive.ipac.caltech.edu/TAP/sync?format=csv&query="
get('nea_ps_box.csv',nea+q(f"select pl_name,hostname,ra,dec,pl_orbper,disc_facility,default_flag from ps where {box}"))
get('nea_k2pandc_box.csv',nea+q(f"select pl_name,epic_hostname,epic_candname,ra,dec,pl_orbper,disposition,disp_refname from k2pandc where {box}"))
get('nea_toi_box.csv',nea+q(f"select toi,tid,ra,dec,pl_orbper,tfopwg_disp from toi where {box}"))
get('nea_k2names.csv',nea+q("select * from k2names where epic_id like '%201395714%'"))
sq=f"SELECT main_id,ra,dec,otype,DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',{ra},{dec}))*3600 AS sep FROM basic WHERE CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},{2/60}))=1"
get('simbad_2arcmin.csv',"https://simbad.cds.unistra.fr/simbad/sim-tap/sync?request=doQuery&lang=adql&format=csv&query="+q(sq))
for nm,i in [('epic','EPIC 201395714'),('tic','TIC 349446806'),('gaia','Gaia DR3 3697661388078573952'),('2mass','2MASS J12153638-0101354'),('ucac4','UCAC4 445-054690')]:
    get(f'simbad_id_{nm}.txt',"https://simbad.cds.unistra.fr/simbad/sim-id?output.format=ASCII&Ident="+q(i))
get('exofop_toi.csv','https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv')
get('exofop_ctoi.csv','https://exofop.ipac.caltech.edu/tess/download_ctoi.php?sort=ctoi&output=csv')
get('exofop_tic349446806.json','https://exofop.ipac.caltech.edu/tess/target.php?id=349446806&json')
