<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col"></div>
        <div class="col-6">
          <b-jumbotron header="Введите текст" lead="Помощник по вводу текста">
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

// import axios from "axios";

// function playByteArray(byteArray) {
//   const arrayBuffer = new ArrayBuffer(byteArray.length);
//   const bufferView = new Uint8Array(arrayBuffer);
//   for (let i = 0; i < byteArray.length; i++) {
//     bufferView[i] = byteArray[i];
//   }
//   const context = new AudioContext();
//   context.decodeAudioData(arrayBuffer, (buffer) => {
//     const source = context.createBufferSource();
//     source.buffer = buffer;
//     source.connect(context.destination);
//     source.start(0);
//   });
// }

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
  return result;
}

async function uploadFileRequest(file) {
  const fileData = new FormData();
  const filename = new Date().toISOString();
  fileData.append("file", file, filename);
  const result = await sendPost("sound", fileData);
  console.log(result);
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
      messages: [
        { text: "Привет человек!", isBot: true },
        { text: "Привет Бот!", isBot: false },
        { text: "Как дела?", isBot: true },
        { text: "Нормально!", isBot: false },
        { text: "Привет человек!", isBot: true },
        { text: "Привет Бот!", isBot: false },
        { text: "Как дела?", isBot: true },
        { text: "Нормально!", isBot: false },
      ],
    };
  },
  computed: {},
  methods: {
    pushMessage(messages) {
      if (messages && messages.length) {
        messages.forEach((it) => {
          console.log(it);
          this.messages.push(it);
        });
      }
    },
    async sendMessage() {
      if (this.text) {
        console.log(this.text);
        const messages = await uploadTextRequest(this.text);
        this.pushMessage(messages);
        this.text = "";
      }
    },
    async setMessages(blob) {
      const messages = await uploadFileRequest(blob);
      this.pushMessage(messages);
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
</style>
