FROM python:3.7-buster

RUN apt-get update && apt-get upgrade -y && apt-get install -y wget && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && \
    apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf --no-install-recommends && \
    pip install requests urllib3 fake-useragent beautifulsoup4 arrow furl parsel websockets html2text tld pytz xlwt aiohttp pymongo pyee appdirs tqdm && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/pip/*

