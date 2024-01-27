import '/src/assets/main.css';
import '/node_modules/bootstrap/dist/css/bootstrap.min.css';
import { createApp } from '/node_modules/.vite/deps/vue.js?v=2584e159';
import App from '/src/App.vue';
import router from '/src/router/index.js'; // Import your router configuration

const app = createApp(App);

app.use(router); // Use the router

app.mount('#app');