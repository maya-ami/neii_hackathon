FROM debian:9.8

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        g++ \
        make \
        automake \
        autoconf \
        bzip2 \
        unzip \
        wget \
        sox \
        libtool \
        git \
        subversion \
        python2.7 \
        python3 \
        zlib1g-dev \
        ca-certificates \
        gfortran \
        patch \
        ffmpeg \
	vim && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python2.7 /usr/bin/python

RUN git clone --depth 1 https://github.com/kaldi-asr/kaldi.git /opt/kaldi && \
    cd /opt/kaldi && \
    cd /opt/kaldi/tools && \
    ./extras/install_mkl.sh && \
    make -j $(nproc) && \
    cd /opt/kaldi/src && \
    ./configure --shared && \
    make depend -j $(nproc) && \
    make -j $(nproc)

RUN apt-get install -y python3-pip python3-setuptools

RUN mkdir /asr

COPY . asr/
ADD ./exp asr/exp
ADD ./local asr/local

RUN chmod +x asr/decode.sh
RUN chmod -R a+rx asr/
RUN chmod -R a+rx asr/exp/
RUN chmod -R a+rx asr/exp/tdnn/
RUN chmod -R a+rx asr/local/

WORKDIR /asr/

CMD ["python3", "stt_server.py"]
