<template>
    <div class="grid-view">
        <div v-for="item in items.slice().reverse()" :key="item.id" class="grid-item">
          <img v-if="item.imageURL != '' | item.imageURL == null" style="border-radius: 2px; object-fit: cover; height: 90%; width: 100%;" :src="item.imageURL" data-bs-toggle="modal" data-bs-target="#detailModal" @click="this.handleSelectedItem(item)">
          <img v-else style="opacity: 0.8; padding: 40px; border-radius: 2px; object-fit: cover; height: 95%; width: 100%;" src="./icons/IconPlaceholder.jpeg">

          <div v-if="item.imageURL != '' | item.imageURL == null" class="d-flex pt-1 ps-2" style="width: 100%">
          <text class="fw-bold" style="font-size: 15px;">${{item.price}}</text>
          <text class="fw-normal ms-3" style="font-size: 14px;">Selling {{item.item}}</text>
          <img class="mt-1 me-1" style="width: 16px; height: 16px; margin-left:auto;" src="./icons/IconVerified.png">
        </div>
        </div>
    </div>
    <!-- Floating Action Button -->
    <div class="fab" data-bs-toggle="modal" data-bs-target="#exampleModal">
        <button @click="handleFabClick">+</button>
    </div>

    <div class="modal" id="detailModal" tabindex="-1" v-if="this.selectedItem!=null">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header p-2 ms-2 mt-1">
            <h3 class="pt-1 pb-0 mb-0">🏷️</h3>
            <h5 class="modal-title fw-bold">&nbsp; &nbsp;Selling {{this.selectedItem.item}}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <img class="mb-3" :src="this.selectedItem.imageURL" style="height: 50vh; width: 100%; object-fit: cover;" >
            <text class="fw-bold d-block">${{this.selectedItem.price}}</text>
            <text class="fw-bold" style="font-size:15px;">Category - {{this.selectedItem.category}}</text>
            <p class="mt-2">{{this.selectedItem.desc}}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header mt-2 p-1">
          <img class="ms-1" style="height: 40px; padding: 0px" src="./icons/IconBlitz.png">
          <h1 class="modal-title fs-3 fw-bold ms-0" id="exampleModalLabel">Blitz Post</h1><p style="font-size:11px" class="ms-2">Powered by AI</p>
          <button type="button" class="btn-close me-1" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <!-- Display the uploaded image here -->
            <img style="border-radius: 8px; height: 50vh; width: 50vw; object-fit: cover;" v-if="uploadedFile" :src="uploadedFileUrl" alt="Uploaded Image" class="img-fluid">
            <div class="mb-3">
              <label for="formFile" class="form-label mt-3 fw-bold">{{ upload_title }}</label>
              <div class="d-flex" style="margin-top: -15px; align-items: center" v-if="uploadedFile">
                 <text style="font-size:15px; text-align: center;">Suggested Category: {{ suggested_category }}</text>
                 <a type="button" class="btn btn-light mb-1 mt-1" style="font-size:14px; text-align: center; margin-left: auto">Select Manual</a>
              </div>
              <input class="form-control mt-1" type="file" id="formFile" @change="handleImageUpload">
            </div>
          </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="close" data-bs-dismiss="modal">Discard</button>
          <button type="button" class="btn btn-primary" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal">Next</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-3 fw-bold" id="exampleModalToggleLabel2">✨ Finalize</h1>
          <button type="button" class="btn-close me-1" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <a style="display: block; font-weight: 600;">Price</a>
          <input type="number" class="" style="padding: 8px; min-height: 50px; min-width: 100%;" v-model="price" placeholder="Enter price here" />
          <a style="display: block; font-weight: 600; margin-top: 15px">Keywords</a>
          <input class="" style="padding: 8px; min-height: 50px; min-width: 100%;" type="text" v-model="this.keywords" placeholder="Please separate keywords with a comma ( , )" />
          <button type="button" class="btn btn-dark mt-2" @click="handlePreviewButton">Generate</button>
          <a v-if="this.description!=''" style="display: block; font-weight: 600; margin-top: 15px">Preview</a>
          <p v-if="this.description!=''" class="" style="padding: 8px; min-height: 50px; min-width: 100%;" type="text">{{ this.description }}</p>
        </div>
        <div class="modal-footer">
          <button class="btn btn-light" data-bs-target="#exampleModal" data-bs-toggle="modal">Back</button>          
          <button v-if="this.description!=''" type="button" class="btn btn-primary ms-1" data-bs-dismiss="modal" @click="post">Post</button>
        </div>  
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import Item from './Item.vue';

export default {

    data() {
        return {
            id: 100,
            description: "",
            suggested_category: "",
            upload_title: "Select photo",
            uploadedFile: null,
            keywords: "",
            selectedItem: null, 
            detected_item: "none",
            items: [
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},               
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},               
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},      
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},               
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
                { id: 0, name: 'Item 0', price: 50, desc: "Some description...", imageURL: ""},
            ],
        };
    },
    computed: {
    uploadedFileUrl() {
      // Return the URL of the uploaded image if available
      console.log(URL.createObjectURL(this.uploadedFile))
      return this.uploadedFile ? URL.createObjectURL(this.uploadedFile) : '';
    },
  },
    methods: {
        post(){
          this.items.push({id: this.id, price: this.price, desc: this.description, imageURL: this.uploadedFileUrl, item: this.detected_item, category: this.suggested_category})
          this.id += 1;
          this.upload_title = "Select photo"
          this.uploadedFile = ""
          this.keywords = ""
          this.description = ""
          this.price = ""
          this.suggested_category = ""
        },
        handleImageUpload(event) {
            this.uploadedFile = event.target.files[0];
            this.uploadImage()
        },
        async handlePreviewButton() {

          const params = {
            suggested_category: this.suggested_category,
            item: this.detected_item,
            keywords: this.keywords,
            // Add more parameters as needed
          };

          const response = await axios.post('http://localhost:8080/auto_complete', params, {
            headers: {
              'Content-Type': 'application/json', // Set the content type for file upload
            },
          });
          
          this.description = response.data
        },
        async uploadImage() {
      // Check if a file was uploaded
      if (this.uploadedFile) {
        // Create a FormData object to send the file in the request body
        const formData = new FormData();
        formData.append('image', this.uploadedFile);

        try {
          // Make an HTTP POST request to your Python API endpoint
          const response = await axios.post('http://localhost:8080/detect_object', formData, {
            headers: {
              'Content-Type': 'multipart/form-data', // Set the content type for file upload
            },
          });

          // Handle the response from the backend (e.g., process results)
          console.log('Response from backend:', response.data[0]);
          this.detected_item = response.data[0];
          this.upload_title = "Detected Item: " + response.data[0].charAt(0).toUpperCase() + response.data[0].slice(1);
          this.suggested_category = response.data[1]

        } catch (error) {
          // Handle any errors that may occur during the request
          console.error('Error:', error);
        }
      } else {
        // Handle the case when no file is selected
        // You can display an error message to the user
        this.upload_title = 'Select photo'
        console.log('No file selected.');
      }
    },
    close() {
        this.uploadedFile = null
        this.upload_title = "Select photo"
        const fileInput = document.getElementById('formFile');
        if (fileInput) {
            fileInput.value = ''; // Clear the selected file
        }
    },
    handleSelectedItem(item) {
      this.selectedItem = item
    },
    },
};
</script>

<style>
body{
  background: #ededed; /* not apply if you go from page-1 to page-2 */
}

.btn{
  font-size: 15px;
}
</style>

<style scoped>
.grid-view {
    position: fixed;
    top: 65px;
    left: 265px;
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    overflow-y: auto;
    right: 0;
    padding-right: 15px;
    padding-bottom: 100px;
    max-height: 100vh;
    gap: 6px;
}

.grid-item {
    background-color: #ffffff;
    border-radius: 2px;
    padding: 0px;
    height: 15vw;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
}

.fab {
    position: fixed;
    bottom:45px;
    right: 45px;
}

.fab button {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 25%;
    width: 65px;
    height: 65px;
    font-size: 30px;
    padding-bottom:5px;
    cursor: pointer;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.fab button:focus {
    outline: none;
}
</style>