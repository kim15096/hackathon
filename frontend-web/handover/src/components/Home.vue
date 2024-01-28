<template>
    <div class="grid-view">
        <div class="items-item">
            <Item />
        </div>
        <div v-for="item in items" :key="item.id" class="grid-item">
            <div class="mb-5">       
                <text>Date Posted: {{ item.date_posted }}</text>
            </div>
            {{ item.name }}
        </div>
    </div>
    <!-- Floating Action Button -->
    <div class="fab" data-bs-toggle="modal" data-bs-target="#exampleModal">
        <button @click="handleFabClick">+</button>
    </div>

    <!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5 fw-bold" id="exampleModalLabel">Create listing</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <!-- Display the uploaded image here -->
            <img v-if="uploadedFile" :src="uploadedFileUrl" alt="Uploaded Image" class="img-fluid">
            <div class="mb-3">
              <label for="formFile" class="form-label mt-2 fw-bold">{{ upload_title }}</label>
              <div v-if="uploadedFile">
                 <text>Suggested Category: {{ suggested_category }}</text>
              </div>
              <input class="form-control" type="file" id="formFile" @change="handleImageUpload">
            </div>
          </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="close" data-bs-dismiss="modal">Discard</button>
          <button type="button" class="btn btn-primary" @click="next">Next</button>
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
            suggested_category: "",
            upload_title: "Select photo",
            uploadedFile: null,
            items: [
                { id: 1, name: 'Item 1' , date_posted:'5.5.5.5'},
                { id: 2, name: 'Item 2' },
                { id: 3, name: 'Item 3' },                
                { id: 12, name: 'Item 1' },
                { id: 22, name: 'Item 2' },
                { id: 32, name: 'Item 3' },
                { id: 13, name: 'Item 1' },
                { id: 23, name: 'Item 2' },
                { id: 33, name: 'Item 3' },
                { id: 14, name: 'Item 1' },
                { id: 24, name: 'Item 2' },
                { id: 34, name: 'Item 3' },                
                { id: 15, name: 'Item 1' },
                { id: 25, name: 'Item 2' },
                { id: 35, name: 'Item 3' },
                { id: 16, name: 'Item 1' },
                { id: 26, name: 'Item 2' },
                { id: 36, name: 'Item 3' },
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
        handleImageUpload(event) {
            this.uploadedFile = event.target.files[0];
            this.uploadImage()
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
          this.upload_title = "Detected item: " + response.data[0].charAt(0).toUpperCase() + response.data[0].slice(1);
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
    closeImageUploadDialog() {
      this.$emit('close');
    },
    },
};
</script>

<style>
body{
  background: #ededed; /* not apply if you go from page-1 to page-2 */
}
</style>

<style scoped>
.grid-view {
    position: fixed;
    top: 65px;
    left: 315px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    overflow-y: auto;
    right: 0;
    padding-right: 15px;
    max-height: 58vw;
    gap: 16px;
}

.grid-item {
    background-color: #ffffff;
    padding: 100px;
    border-radius: 6px;
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
    border-radius: 30%;
    width: 70px;
    height: 70px;
    font-size: 30px;
    cursor: pointer;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.fab button:focus {
    outline: none;
}
</style>