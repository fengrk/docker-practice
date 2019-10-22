FROM ubuntu:18.04

RUN		apt update && apt install -y curl git vim gnupg2 && \
		mkdir -p /code/ && cd /code/ && \
		curl -sL https://deb.nodesource.com/setup_11.x  | bash - && \
        apt install -y nodejs && \
        curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg |  apt-key add - && \
		echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
		git clone https://github.com/SeleniumHQ/selenium-ide && \
		apt update && apt install -y yarn  && \ 
		cd /code/selenium-ide && yarn && yarn build && yarn watch && \
		rm -rf /var/lib/apt/lists/*

