FROM phusion/baseimage:0.10.1

RUN install_clean git scons build-essential libao4 libao-dev pkg-config flite1-dev libao-dev portaudio19-dev lame python3 python3-pip python3-setuptools locales locales-all sox && \
    git clone https://github.com/Olga-Yakovleva/RHVoice.git /opt/RHVoice && \
    cd /opt/RHVoice && git checkout ee8be30 && scons && scons install && ldconfig && \
    pip3 install flask pymorphy2 && \
    cd /opt && rm -rf /opt/RHVoice && mkdir data && \
    apt-get purge -y build-essential scons pkg-config binutils bzip2 cpp cpp-5 dpkg-dev g++ g++-5 gcc gcc-5 libdpkg-perl libgcc-5-dev libstdc++-5-dev make uuid-dev

ENV LC_ALL ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU.UTF-8

COPY app.py /opt/app.py

EXPOSE 5555

CMD ["python3", "/opt/app.py"]
