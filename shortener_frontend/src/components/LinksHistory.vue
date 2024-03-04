<template>
  <div class="links-history" v-if="lastLinks.length != 0">
    <h5>Last links</h5>

    <div class="rounded-box-last-links-history">
      <div class="last-link-box" v-for="link in lastLinks" :key="link">
        <div class="row">
          <div class="column-left">
            <a :href="link.urlOriginal" class="original-url" target="_blank">{{
              link.urlOriginal
            }}</a>
            <a
              :href="link.urlShortened"
              class="shortened-url"
              target="_blank"
              >{{ link.urlShortened }}</a
            >
          </div>
          <div class="column-right">
            <div
              class="icon"
              @click.prevent="copyUrlShortened(link.urlShortened)"
            >
              <FileMultipleOutline />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FileMultipleOutline from "vue-material-design-icons/FileMultipleOutline.vue";

import { copyUrlShortened } from "@/utils.js";

export default {
  props: {
    lastLinks: { Object },
  },
  components: {
    FileMultipleOutline,
  },
  methods: {
    copyUrlShortened,
  },
};
</script>

<style scoped>
.links-history {
  margin-top: 20px;
}

.rounded-box-last-links-history {
  border: solid #cbcfd4 1px;
  border-radius: 25px;
  width: 50vh;
  padding: 20px;
  margin-top: 20px;
  align-items: stretch;
}

h5 {
  font-size: small;
  display: flex;
  margin-left: 30px;
  margin-bottom: 0;
}

.last-link-box {
  border-radius: 25px;
  padding: 20px;
  background-color: #ffffff;
  margin-top: 10px;
  box-shadow: 0 0 10px rgba(54, 60, 86, 0.07);
}

.last-link-box .row {
  display: flex;
  align-items: center;
}

.last-link-box .column-left {
  flex: 4;
}

.last-link-box .column-right {
  flex: 1;
}

.last-link-box .original-url {
  display: flex;
  font-size: smaller;
  color: #495b6d !important;
  margin-left: 5px;
  margin-bottom: 8px;
}

.last-link-box .shortened-url {
  display: flex;
  color: #4a24ac;
  text-decoration: none;
  font-weight: bolder;
  font-size: smaller;
  margin-left: 5px;
  font-size: smaller;
}

.last-link-box .icon {
  text-align: right;
  font-size: smaller;
  cursor: pointer;
  color: #495b6d;
}
</style>
