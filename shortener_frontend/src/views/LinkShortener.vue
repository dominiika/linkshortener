<template>
  <div class="container">
    <div class="rounded-box-link-shortener">
      <img
        src="@/assets/center_ai_logo.png"
        alt="Center_ai logo"
        class="centered-image"
      />
      <form @submit.prevent="submitUrl">
        <h3>Short link</h3>
        <label
          for="urlOriginal"
          :class="{ 'error-label': v$.urlOriginal.$error }"
          >Link to shortcut</label
        >
        <input
          id="urlOriginal"
          type="text"
          v-model="urlOriginal"
          placeholder="Enter URL"
          :class="{ 'error-input': v$.urlOriginal.$error }"
        />
        <div class="input-errors" v-if="v$.urlOriginal.$errors.length">
          <div
            class="error-msg"
            v-for="error of v$.urlOriginal.$errors"
            :key="error.$uid"
          >
            {{ error.$message }}
          </div>
        </div>
        <button type="submit">Shorten it</button>
      </form>

      <div class="link-shortened-box" v-if="urlShortened">
        <div class="row">
          <div class="column-left">
            <a :href="urlShortened" target="_blank" class="link"
              ><span class="text">{{ urlShortened }}</span></a
            >
          </div>
          <div class="column-right">
            <span class="icon" @click.prevent="copyUrlShortened(urlShortened)"
              ><FileMultipleOutline
            /></span>
          </div>
        </div>
      </div>
    </div>
    <LinksHistory :lastLinks="lastLinks" />
  </div>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import { required, url, helpers } from "@vuelidate/validators";
import FileMultipleOutline from "vue-material-design-icons/FileMultipleOutline.vue";

import LinksHistory from "@/components/LinksHistory.vue";
import { copyUrlShortened } from "@/utils.js";

export default {
  setup() {
    return { v$: useVuelidate() };
  },
  components: {
    FileMultipleOutline,
    LinksHistory,
  },
  data() {
    return {
      urlOriginal: null,
      urlShortened: null,
      lastLinks: [],
    };
  },
  methods: {
    copyUrlShortened,
    async submitUrl() {
      this.v$.urlOriginal.$touch();
      if (!this.v$.urlOriginal.$invalid) {
        try {
          const response = await this.$axios.post("links/", {
            original_url: this.urlOriginal,
            user_metadata: this.getUserMetaData(),
          });
          this.urlShortened = response.data.shortened_url;
          this.addToHistory();
        } catch (error) {
          console.error("Error:", error);
        }
      }
    },
    getUserMetaData() {
      return {
        userAgent: navigator.userAgent,
        languages: navigator.languages,
      };
    },
    addToHistory() {
      let data = {
        urlOriginal: this.urlOriginal,
        urlShortened: this.urlShortened,
      };

      let lastLinks = JSON.parse(localStorage.getItem("lastLinks"));
      if (lastLinks == null) {
        lastLinks = [data];
      } else {
        lastLinks.unshift(data);
        if (lastLinks.length > 3) {
          lastLinks.pop();
        }
      }

      localStorage.setItem("lastLinks", JSON.stringify(lastLinks));
      this.lastLinks = lastLinks;
    },
    loadHistory() {
      const lastLinks = JSON.parse(localStorage.getItem("lastLinks"));
      if (lastLinks) {
        this.lastLinks = lastLinks;
      }
    },
  },
  validations() {
    return {
      urlOriginal: {
        required: helpers.withMessage("This field is required.", required),
        url: helpers.withMessage("This field must be a valid URL.", url),
      },
    };
  },
  mounted() {
    this.loadHistory();
  },
};
</script>

<style scoped>
.container {
  background-color: #fafafa;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  flex-direction: column;
}

.rounded-box-link-shortener {
  background-color: #ffffff;
  border-radius: 25px;
  width: 50vh;
  padding: 20px;
  padding-bottom: 40px;
  box-shadow: 0 0 10px rgba(54, 60, 86, 0.07);
  align-items: stretch;
}

.centered-image {
  max-width: 100%;
  max-height: 100%;
}

.rounded-box-link-shortener form {
  display: flex;
  flex-direction: column;
}

.rounded-box-link-shortener label {
  color: #4a24ac;
  text-align: left;
  font-size: small;
}

.error-label {
  color: #b71c1c !important;
}

.rounded-box-link-shortener input {
  padding: 10px;
  padding-left: 0;
  margin-bottom: 10px;
  border: none;
  border-bottom: solid #4a24ac 1px;
  background-color: #ffffff;
  cursor: pointer;
  color: #2c3e50;
}

.error-input {
  border-bottom-color: #b71c1c !important;
}

.input-errors {
  margin-bottom: 10px;
}

.error-msg {
  color: #b71c1c;
  font-size: smaller;
  text-align: left;
}

.rounded-box-link-shortener button {
  padding: 10px;
  background-color: #4a24ac;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 40px;
  margin-top: 10px;
}

.link-shortened-box {
  margin-top: 30px;
  background-color: #fafafa;
  border-radius: 10px;
  padding: 5px;
}

.link-shortened-box .row {
  display: flex;
  align-items: center;
}

.link-shortened-box .column-left {
  flex: 4;
}

.link-shortened-box .column-right {
  flex: 1;
}

.link-shortened-box .link {
  display: flex;
  color: #4a24ac;
  font-weight: bolder;
  font-size: smaller;
  text-align: left;
}

.link-shortened-box .text {
  margin-right: 10px;
}

.link-shortened-box .icon {
  right: 0;
  font-size: smaller;
  color: #495b6d;
  cursor: pointer;
}
</style>
