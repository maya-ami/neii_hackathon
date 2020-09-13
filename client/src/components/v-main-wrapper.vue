<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col"></div>
        <div class="col-6">
          <b-jumbotron class="pt-4 pb-4">
            <h3 class="display-4">Sovet</h3>
            <p>Поможет Вам узнать о мерах социальной поддержки</p>
            <b-list-group v-if="messages">
              <b-list-group-item v-for="(msg, index) of messages" :key="index">
                <p :class="{ 'text-left': msg.isBot, 'text-right': !msg.isBot }">{{msg.text}}</p>
                <audio :src="audio" autoplay="autoplay" />
              </b-list-group-item>
            </b-list-group>
            <hr class="my-4" />
            <div class="row">
              <div class="col-sm-8">
                <b-form-input v-model="text" placeholder="Введите текст запроса"></b-form-input>
              </div>
              <b-button variant="primary" href="#" @click="sendTextMessage">Отправить текст</b-button>
            </div>
            <hr class="my-4" />
            <div class="row">
              <div class="col-sm-5"></div>
              <div class="col-sm-1">
                <vRecorderAudio @receivingMessage="sendSoundMessage" />
              </div>
            </div>
          </b-jumbotron>
        </div>
        <div class="col"></div>
      </div>
    </div>
  </div>
</template>
<script>
import vRecorderAudio from "./v-recorder-audio.vue";

async function sendPost(path, formData) {
  const response = await fetch(`http://localhost:8083/${path}`, {
    method: "POST",
    body: formData,
  });
  const result = await response.formData();
  const obj = {};
  for (var pair of result.entries()) {
    obj[pair[0]] = pair[1];
  }
  return obj;
}

async function uploadTextRequest(text) {
  const data = { text };
  const formData = new FormData();

  for (const name in data) {
    formData.append(name, data[name]);
  }
  const result = await sendPost("text", formData);
  if (result["messages"]) {
    result["messages"] = JSON.parse(result["messages"]);
  }
  return result;
}

async function uploadFileRequest(file) {
  const fileData = new FormData();
  const filename = new Date().toISOString();
  fileData.append("file", file, filename);
  const result = await sendPost("sound", fileData);
  if (result["messages"]) {
    result["messages"] = JSON.parse(result["messages"]);
  }
  return result;
}

export default {
  name: "v-main-wrapper",
  components: { vRecorderAudio },
  props: {},
  data() {
    return {
      title: "Main wrapper",
      text: "",
      messages: [],
      audio: null,
    };
  },
  computed: {},
  methods: {
    pushMessage(messages) {
      if (messages && messages.length) {
        messages.forEach((it) => this.messages.push(it));
      }
    },
    scrollToEnd() {
      const container = this.$el.querySelector(".list-group");
      if (container) {
        setTimeout(() => {
          const y = container.scrollHeight + 1000;
          container.scrollTo(0, y);
        }, 100);
      }
    },
    setAudio({ files } = {}) {
      if (files) {
        const url = URL.createObjectURL(files);
        this.audio = url;
      }
    },
    async sendTextMessage() {
      if (this.text) {
        this.pushMessage([{ text: this.text, isBot: false }]);
        const result = await uploadTextRequest(this.text);
        this.setAudio(result);
        this.pushMessage(result.messages);
        this.scrollToEnd();
        this.text = "";
      }
    },
    async sendSoundMessage(blob) {
      const result = await uploadFileRequest(blob);
      this.setAudio(result);
      this.pushMessage(result.messages);
      this.scrollToEnd();
    },
  },
};
</script>
<style lang="scss">
.v-main-wrapper {
  max-width: 900px;
  margin: 0 auto;
}
.list-group {
  max-height: 300px;
  margin-bottom: 10px;
  overflow: scroll;
  overflow-y: auto;
  overflow-x: auto;
}
.jumbotron {
  background-color: azure;
  padding: 2rem 1rem;
}
</style>
