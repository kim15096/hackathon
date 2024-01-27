import '/src/assets/main.css';
import '/node_modules/bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap'
import { createApp } from 'vue';
import App from '/src/App.vue';
import router from '/src/router/index.js'; // Import your router configuration

const app = createApp(App);

app.use(router); // Use the router

app.mount('#app');