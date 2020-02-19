<template>
  <div>
    <ul>
      <li v-for="(todo) in todoItems" :key="todo.todo">
        {{ todo.todo }}
        <button @click="deleteTodo(todo)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['todoItems'],
  data() {
    return {
      // todoId: this.todoItems.id,
    }
  },
  methods: {
    deleteTodo(index) {
      this.$emit('deleteTodo', index)
      
      // const target = event.target
      // console.log(target.id, typeof target.id)
      // target.id 로 기능개선 했음!
      // this.$emit('deleteTodo', target.id)
    }
  }
  
}
</script>

<style scoped>

</style>