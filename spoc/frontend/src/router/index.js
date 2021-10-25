import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import StudentLogin from '../components/Student/StudentLogin'
import StudentRegister from '../components/Student/StudentRegister'
import StudentHead from '../components/Student/StudentHead'
import TeacherLogin from '../components/Teacher/TeacherLogin'
import TeacherHead from '../components/Teacher/TeacherHead'
import TeacherRegister from '../components/Teacher/TeacherRegister'
import SelectCourse from '../components/Student/SelectCourse'
import StudentCourse from '../components/Student/StudentCourse'
import TeacherCourse from '../components/Teacher/TeacherCourse'
import BuildCourse from '../components/Teacher/BuildCourse'
import AllCourse from '../components/Teacher/AllCourse'
import StudentChange from '../components/Student/StudentChange'
import TeacherChange from '../components/Teacher/TeacherChange'

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
    },
    {
      path: '/SelectCourse',
      name: 'SelectCourse',
      component: SelectCourse
    },
    {
      path: '/StudentCourse',
      name: 'StudentCourse',
      component: StudentCourse
    },
    {
      path: '/BuildCourse',
      name: 'BuildCourse',
      component: BuildCourse
    },
    {
      path: '/TeacherCourse',
      name: 'TeacherCourse',
      component: TeacherCourse
    },
    {
      path: '/AllCourse',
      name: 'AllCourse',
      component: AllCourse
    },
    {
      path: '/StudentChange',
      name: 'StudentChange',
      component: StudentChange
    },
    {
      path: '/TeacherChange',
      name: 'TeacherChange',
      component: TeacherChange
    }
  ]
})
