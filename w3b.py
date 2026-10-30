import asyncio,json,re,html,datetime,collections
import bot,discovery,practice,intake
TODAY=discovery.TODAY
def pub_meta(body):
    for name,pat in (('JSON-LD datePublished',r'"datePublished"\s*:\s*"(\d{4}-\d\d-\d\d)'),('article:published_time',r'article:published_time"\s+content="(\d{4}-\d\d-\d\d)'),('time[datetime]',r'<time[^>]+datetime="(\d{4}-\d\d-\d\d)')):
        m=re.search(pat,body)
        if m: return m.group(1),name
    return None,None
async def go():
    read,b,p=await discovery.browser_reader(); day=discovery.Day('florida','Timothy A. Edick',read); day.Q=json.load(open('florida-intake-queue.json')); Q=day.Q; day.third=10**6; day.spent={'Acquisitions':0,'Private Equity':0,'Fractionals':0}
    bot.RUN_START=datetime.datetime.now(datetime.timezone.utc).date().isoformat(); out={'articles_read':0,'queued':0,'no_date':0,'no_sentence':0,'refused':0}
    x=await day.one_read('Acquisitions','gnews_rss','https://news.google.com/rss/search?q=%22Florida%22+company+acquired&hl=en-US&gl=US&ceid=US:en')
    if not x[0]: print('feed refused'); return
    items=re.findall(r'<item>(.*?)</item>',x[2],re.S); got=[]
    for it in items:
        ttl=re.sub(r'<[^>]+>','',(re.search(r'<title>(.*?)</title>',it,re.S) or [None,''])[1]).strip(); link=(re.search(r'<link>(.*?)</link>',it,re.S) or re.search(r'<guid[^>]*>(.*?)</guid>',it,re.S)); link=html.unescape(link.group(1).strip()) if link else ''; pd=(re.search(r'<pubDate>(.*?)</pubDate>',it,re.S) or [None,None])[1]
        if re.search(r'\bFlorida\b|\bFL\b|Miami|Tampa|Orlando|Jacksonville|Fort Lauderdale|Boca Raton|West Palm',ttl,re.I) and re.search(practice.KW['Acquisitions'],ttl,re.I): got.append((ttl,link,pd))
    seen={v.get('feed_title') for v in Q.values()}
    try:
        for ttl,link,pd in got:
            if ttl in seen or not link: continue
            if bot.reads_today()>=bot.CEILING-2: break
            x=await day.one_read('Acquisitions','gnews_rss:article',link); out['articles_read']+=1
            if not x[0]: out['refused']+=1; continue
            body=x[2]; d,f=pub_meta(body)
            if not d and pd and re.match(r'\w{3}, \d{1,2} \w{3} \d{4}',pd.strip()): d=datetime.datetime.strptime(pd.strip()[:25],'%a, %d %b %Y %H:%M:%S').date().isoformat(); f='feed pubDate'
            if not d: out['no_date']+=1; continue
            txt=re.sub(r'<script.*?</script>|<style.*?</style>','',body,flags=re.S|re.I); txt=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',txt)))
            sent=next((s_.strip() for s_ in re.split(r'(?<=[.!?])\s+',txt) if re.search(practice.KW['Acquisitions'],s_,re.I) and re.search(r'\bFlorida\b|\bFL\b|Miami|Tampa|Orlando|Jacksonville|Fort Lauderdale|Boca|West Palm',s_)),None)
            if not sent: out['no_sentence']+=1; continue
            k=day.queue_candidate('Acquisitions',{'id':'gnews_rss','name':'Google News RSS'},None,link,sent,d,None)
            if k not in ('filtered','on file'): Q[k]['date_field']=f; Q[k]['feed_title']=ttl; out['queued']+=1
    except bot.Refused as e: out['stopped']=str(e)
    json.dump(Q,open('florida-intake-queue.json','w'),indent=1,ensure_ascii=False); json.dump(out,open('reports/w3-feed-continuation.json','w'),indent=1); print(out); await b.close(); await p.stop()
asyncio.run(go())
