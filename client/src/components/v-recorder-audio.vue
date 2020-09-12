<template lang="html">
  <div
    v-if="isSupported"
    class="v-recorder-audio"
    :class="{
      active: isRecording
    }"
    @mousedown="startRecording"
    @mouseleave="stopRecording"
    @mouseup="stopRecording"
    @touchstart="startRecording"
    @touchend="stopRecording"
    @touchcancel="stopRecording"
  >
    <span></span>
  </div>
</template>

<script>
import Recorder from "@/utils/recorder.js";

export default {
  name: "v-recorder-audio",
  data() {
    return {
      isSupported: false,
      hasPermission: false,
      isRecording: false,
      isPaused: false,
      gumStream: Object,
      rec: Object,
    };
  },
  methods: {
    stopRecording() {
      return this.stop();
    },
    startRecording() {
      return this.start();
    },

    async start() {
      if (this.isRecording) {
        return;
      }
      this.isRecording = true;
      console.log("recordButton clicked");
      const constraints = { audio: true, video: false };
      navigator.mediaDevices
        .getUserMedia(constraints)
        .then((stream) => {
          const audioContext = new AudioContext();
          console.log(
            `"Format: 1 channel pcm @ ${audioContext.sampleRate / 1000}kHz"`
          );
          this.gumStream = stream;
          const input = audioContext.createMediaStreamSource(stream);
          this.rec = new Recorder(input, { numChannels: 1 });
          this.rec.record();
          console.log("Recording started");
        })
        .catch((error) => console.error(error));
    },
    stop() {
      if (!this.isRecording) return;
      this.isRecording = false;

      this.rec.stop();
      this.gumStream.getAudioTracks()[0].stop();
      this.rec.exportWAV((blob) => this.$emit("receivingMessage", blob));
    },
  },
  mounted() {
    if (!navigator.mediaDevices && !navigator.mediaDevices.getUserMedia) {
      console.warn("Media Devices are not supported from your browser.");
      return;
    }
    if (!window.MediaRecorder && this.constraints.video) {
      console.warn(
        "MediaRecorder for video is not supported from your browser."
      );
      return;
    }

    this.isSupported = true;
  },
};
</script>

<style lang="scss">
.v-recorder-audio {
  margin: auto;
  position: relative;
  background-color: #4db6ac;
  border-radius: 50%;
  width: 64px;
  height: 64px;
  display: inline-block;
  cursor: pointer;
  box-shadow: 0 0 0 0 rgba(232, 76, 61, 0.7);
  &:hover {
    background-color: #26a69a;
  }
  &.active {
    background-color: #ef5350;
    -webkit-animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);
    -moz-animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);
    animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);
  }
  &:before,
  &:after {
    content: "";
    position: absolute;
    background-color: #fff;
  }
  &:after {
    top: 30%;
    left: 43%;
    height: 15%;
    width: 14%;
    border-top-left-radius: 50%;
    border-top-right-radius: 50%;
  }
  &:before {
    top: 40%;
    left: 43%;
    height: 15%;
    width: 14%;
    border-bottom-left-radius: 50%;
    border-bottom-right-radius: 50%;
  }
  span {
    position: absolute;
    top: 50%;
    left: 36%;
    height: 24%;
    width: 28%;
    overflow: hidden;
    &:before,
    &:after {
      content: "";
      position: absolute;
      background-color: #fff;
    }
    &:before {
      bottom: 50%;
      width: 100%;
      height: 100%;
      box-sizing: border-box;
      border-radius: 50%;
      border: 0.125em solid #fff;
      background: none;
      left: 0;
    }
    &:after {
      top: 50%;
      left: 40%;
      width: 20%;
      height: 25%;
    }
  }
}
@keyframes pulse {
  to {
    box-shadow: 0 0 0 10px rgba(239, 83, 80, 0.1);
    background-color: #e53935;
    transform: scale(0.9);
  }
}
</style>
