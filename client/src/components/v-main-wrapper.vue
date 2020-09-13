<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col"></div>
        <div class="col-6">
          <b-jumbotron>
            <h3 class="display-4">Sovet</h3>
            <p>Поможет Вам узнать о мерах социальной поддержки</p>
            <b-list-group v-if="messages">
              <b-list-group-item v-for="(msg, index) of messages" :key="index">
                <p :class="{ 'text-left': msg.isBot, 'text-right': !msg.isBot }">{{msg.text}}</p>
              </b-list-group-item>
            </b-list-group>
            <hr class="my-4" />
            <div class="row">
              <div class="col-sm-8">
                <b-form-input v-model="text" placeholder="Введите текст запроса"></b-form-input>
              </div>
              <b-button variant="primary" href="#" @click="sendMessage">Отправить текст</b-button>
            </div>
            <hr class="my-4" />
            <div class="row">
              <div class="col-sm-5"></div>
              <div class="col-sm-1">
                <vRecorderAudio @receivingMessage="setMessages" />
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

function playByteArray(byteArray) {
  const arrayBuffer = new ArrayBuffer(byteArray.length);
  const bufferView = new Uint8Array(arrayBuffer);
  for (let i = 0; i < byteArray.length; i++) {
    bufferView[i] = byteArray[i];
  }
  const context = new AudioContext();
  context.decodeAudioData(arrayBuffer, (buffer) => {
    const source = context.createBufferSource();
    source.buffer = buffer;
    source.connect(context.destination);
    source.start(0);
  });
}

async function sendPost(path, formData) {
  const response = await fetch(`http://localhost:8083/${path}`, {
    method: "POST",
    body: formData,
  });
  console.log("Good");
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
  console.log(result);
  if (result["messages"]) {
    result["messages"] = JSON.parse(result["messages"]);
  }
  document.aa = result;
  document.aaa = (b) => playByteArray(b);
  console.log(result["messages"], result);
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
  console.log(result["messages"], result);
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
    };
  },
  computed: {},
  methods: {
    pushMessage(messages) {
      console.log(messages);
      if (messages && messages.length) {
        messages.forEach((it) => {
          console.log(it);
          this.messages.push(it);
        });
      }
    },
    scrollToEnd() {
      const container = this.$el.querySelector(".list-group");
      if (container) {
        setTimeout(() => {
          const y = container.scrollHeight + 1000;
          container.scrollTo(0, y);
        }, 1000);
      }
    },
    async sendMessage() {
      if (this.text) {
        this.pushMessage([{ text: this.text, isBot: false }]);
        console.log(this.text);
        const result = await uploadTextRequest(this.text);
        this.pushMessage(result.messages);
        this.scrollToEnd();
        this.text = "";
      }
    },
    async setMessages(blob) {
      const result = await uploadFileRequest(blob);
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
}
.jumbotron header {
  background-color: red;
}
</style>
