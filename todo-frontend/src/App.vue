<template>
  <div id="app">
    <TodoHeader></TodoHeader>
    <TodoInput @addTodo="addTodo"></TodoInput>
    <TodoList :todoItems="todoItems" @deleteTodo="deleteTodo"></TodoList>
    <TodoFooter @removeAll="removeAll"></TodoFooter>

  </div>
</template>

<script>
import TodoHeader from './components/TodoHeader'
import TodoInput from './components/TodoInput'
import TodoList from './components/TodoList'
import TodoFooter from './components/TodoFooter'

export default {
  name: 'app',
  components: {
    TodoHeader,
    TodoInput,
    TodoList,
    TodoFooter
  },
  data () {
    return {
      // todoItem:'',
      todoItems: [],
    }
  },
  created() {
    this.render()
  },
  methods: {
    render() {
      this.$http.get('http://localhost:8000/api/todos/').then(res => {
        if (res.data !== null && res.data.length !== 0) {
          this.todoItems = res.data        
        } else {
          this.todoItems = []
        }
      })
    },
    addTodo(userTodo) {
      this.$http.post('http://localhost:8000/api/todos/', {'todo': userTodo}).then(res => {
        this.render()
      })
    },
    deleteTodo(todo) {
      this.$http.delete('http://localhost:8000/api/todos/'+ todo.id + '/').then(res => {
        this.render()
      })

    },
    removeAll() {
      this.$http.delete('http://localhost:8000/api/todos/removeAll').then(res => {
        this.render()
      })
    },

  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}



</style>
