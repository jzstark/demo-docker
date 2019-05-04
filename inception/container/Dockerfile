FROM owlbarn/owl:ubuntu

# The user has to be 'opam' instead of root

RUN sudo apt-get -y update && sudo apt-get -y install imagemagick python

ENV GID 9428a62a31dbea75511882ab8218076f
ENV VID 9bc81caa0053cd5e07a0fb148623a3b3ab3257dc

WORKDIR $HOME

RUN  wget -q https://gist.github.com/jzstark/$GID/archive/$VID.zip -O  inception_gist.zip \
     && unzip inception_gist.zip \
     && mv $GID-$VID/ /tmp/inception/

RUN  wget -q https://gist.github.com/jzstark/51eaf74c65fa14c8c466ecfab2351bbd/archive/43e8de51ee1486f4a9a9b3f673da0f59043903a5.zip -O imagenet_cls.zip \
     && unzip imagenet_cls.zip \
     && mv 51eaf74c65fa14c8c466ecfab2351bbd-43e8de51ee1486f4a9a9b3f673da0f59043903a5/* /tmp/inception/


RUN  wget -q https://gist.github.com/jzstark/51eaf74c65fa14c8c466ecfab2351bbd/archive/43e8de51ee1486f4a9a9b3f673da0f59043903a5.zip -O imagenet_cls.zip \
     && unzip imagenet_cls.zip \
     && mv 51eaf74c65fa14c8c466ecfab2351bbd-43e8de51ee1486f4a9a9b3f673da0f59043903a5/* /tmp/inception/


RUN wget https://gist.githubusercontent.com/jzstark/86a1748bbc898f2e42538839edba00e1/raw/a364bc00eec36e8973cdd63671b8ebd55700dd36/imageUtils.ml -O /tmp/inception/imageUtils.ml

RUN cd /tmp/inception/ \
    && sed -i '/^#/ d' *.ml \ 
    && sed -i 's/Owl_zoo_path.extend_zoo_path//g' *.ml \
    && eval `opam config env` \
    && dune build classify.exe

RUN echo "export LD_LIBRARY_PATH=/opt/OpenBLAS/lib:$LD_LIBRARY_PATH" >> /home/opam/.bashrc \
    && bash -c "source /home/opam/.bashrc"

# This dir has to contain weight file

# NOT ENTRYPOINT!!!!
#ENTRYPOINT ["sh", "-c", "export LD_LIBRARY_PATH=/opt/OpenBLAS/lib && /tmp/inception/_build/default/classify.exe" ]  
#CMD ["echo \"fuck\" && export LD_LIBRARY_PATH=/opt/OpenBLAS/lib && /tmp/inception/_build/default/classify.exe" ]  
#CMD ["/tmp/inception/_build/default/classify.exe"]  
#ENTRYPOINT ["/bin/bash", "-c", "LD_LIBRARY_PATH=/opt/OpenBLAS/lib /tmp/inception/_build/default/classify.exe && echo hellp"]
#ENTRYPOINT ["sh", "-c", "LD_LIBRARY_PATH=/opt/OpenBLAS && echo $LD_LIBRARY_PATH && ls && "]

COPY entry.py /tmp/inception/entry.py
WORKDIR "/tmp/inception" 

ENTRYPOINT ["python", "/tmp/inception/entry.py"]
