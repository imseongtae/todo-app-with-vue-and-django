<template>
  <div>
    
    <input type="text" v-model="todoItem" @keypress.enter="addTodo">
    <button @click="addTodo">추가</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todoItem: '',

    }
  },
  methods: {
    addTodo() {
      this.$emit('addTodo', this.todoItem);
      this.clearInput()
    },
    clearInput() {
      this.todoItem = '';
    }
  }

}
</script>

<style scoped>

</style>