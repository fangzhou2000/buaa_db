import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import StudentLogin from '../components/StudentLogin'
import StudentRegister from '../components/StudentRegister'
import StudentHead from '../components/StudentHead'
import TeacherLogin from '../components/TeacherLogin'
import TeacherHead from '../components/TeacherHead'
import TeacherRegister from '../components/TeacherRegister'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/StudentLogin',
      name: 'StudentLogin',
      component: StudentLogin
    },
    {
      path: '/StudentRegister',
      name: 'StudentRegister',
      component: StudentRegister
    },
    {
      path: '/StudentHead',
      name: 'StudentHead',
      component: StudentHead
    },
    {
      path: '/TeacherLogin',
      name: 'TeacherLogin',
      component: TeacherLogin
    },
    {
      path: '/TeacherHead',
      name: 'TeacherHead',
      component: TeacherHead
    },
    {
      path: '/TeacherRegister',
      name: 'TeacherRegister',
      component: TeacherRegister
    }
  ]
})
