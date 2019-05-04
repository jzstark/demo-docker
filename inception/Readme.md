# Usage

- (optional) First, enter `container` directory, build an image. I've already built one that is named `matrixanger/inception`, and will use this name in docker-composer. *Somehow the dockerhub site is down now; I'll update it later. Until then, build it on your own computer and replace the name accordingly in the docker-compose file.*
- Choose a picture on your computer, and **copy the image to the same directory** with the `docker-compose` file.
- Suppose this image is named `foo.jpg`, then run `docker-compose run classify foo.jpg`. 
- A file named `foo.json` will be generated in the same directory. It contains the image classification result. Check the [doc](https://gist.github.com/jzstark/9428a62a31dbea75511882ab8218076f#usage) to see the meaning of this result.
