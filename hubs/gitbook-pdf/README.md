# ref: https://github.com/watahani/gitbook-pdf

```
# install dependencies
docker run --rm -v $(pwd)/sample:/book frkhit/docker-practice:gitbook-pdf gitbook install

# build pdf
docker run --rm -v $(pwd)/sample:/book frkhit/docker-practice:gitbook-pdf gitbook pdf

# build epub
docker run --rm -v $(pwd)/sample:/book frkhit/docker-practice:gitbook-pdf gitbook epub

# serve web page
docker run --rm -v $(pwd)/sample:/book -p 4000:4000 frkhit/docker-practice:gitbook-pdf gitbook serve 

```
