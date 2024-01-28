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
</template>

<script>
import Item from './Item.vue';

export default {
    data() {
        return {
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
};
</script>

<style scoped>
.grid-view {
    position: fixed;
    top: 70px;
    left: 315px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    overflow-y: auto;
    max-height: 58vw;
    gap: 16px;
}

.grid-item {
    background-color: #ececec;
    padding: 112px;
    border-radius: 8px;
}
</style>