import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import StudentLogin from '../components/Student/StudentLogin'
import StudentRegister from '../components/Student/StudentRegister'
import StudentHead from '../components/Student/StudentHead'
import TeacherLogin from '../components/Teacher/TeacherLogin'
import TeacherHead from '../components/Teacher/TeacherHead'
import TeacherRegister from '../components/Teacher/TeacherRegister'
import StudentCourse from '../components/Student/StudentCourse/StudentCourse'
import SelectCourse from '../components/Student/StudentCourse/SelectCourse'
import SelectedCourse from '../components/Student/StudentCourse/SelectedCourse'
import TeacherCourse from '../components/Teacher/TeacherCourse/TeacherCourse'
import ManageCourse from '../components/Teacher/TeacherCourse/ManageCourse'
import ChangeCourse from '../components/Teacher/TeacherCourse/ChangeCourse'
import BuildCourse from '../components/Teacher/TeacherCourse/BuildCourse'
import AllCourse from '../components/Teacher/TeacherCourse/AllCourse'
import StudentChange from '../components/Student/StudentChange/StudentChange'
import TeacherChange from '../components/Teacher/TeacherChange/TeacherChange'
import TeacherMaterial from '../components/Teacher/TeacherMaterial/TeacherMaterial'
import AllMaterial from '../components/Teacher/TeacherMaterial/AllMaterial'
import BuildMaterial from '../components/Teacher/TeacherMaterial/BuildMaterial'
import ManageMaterial from '../components/Teacher/TeacherMaterial/ManageMaterial'
import StudentCommentAndDiscuss from '../components/Student/StudentCommentAndDiscuss/StudentCommentAndDiscuss'
import StudentCourseComment from '../components/Student/StudentCommentAndDiscuss/StudentCourseComment'
import CommentCourse from '../components/Student/StudentCommentAndDiscuss/CommentCourse'

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
      path: '/StudentCourse',
      name: 'StudentCourse',
      component: StudentCourse,
      children: [
        {
          path: 'SelectCourse',
          name: 'SelectCourse',
          component: SelectCourse
        },
        {
          path: 'SelectedCourse',
          name: 'SelectedCourse',
          component: SelectedCourse
        }
      ]
    },
    {
      path: '/TeacherCourse',
      name: 'TeacherCourse',
      component: TeacherCourse,
      children: [
        {
          path: 'BuildCourse',
          name: 'BuildCourse',
          component: BuildCourse
        },
        {
          path: 'ManageCourse',
          name: 'ManageCourse',
          component: ManageCourse
        },
        {
          path: 'AllCourse',
          name: 'AllCourse',
          component: AllCourse
        },
        {
          path: 'ChangeCourse',
          name: 'ChangeCourse',
          component: ChangeCourse
        }
      ]
    },
    {
      path: '/StudentChange',
      name: 'StudentChange',
      component: StudentChange,
      children: [
        {
          path: 'StudentChange',
          component: StudentChange
        }
      ]
    },
    {
      path: '/TeacherChange',
      name: 'TeacherChange',
      component: TeacherChange,
      children: [
        {
          path: 'TeacherChange',
          component: TeacherChange
        }
      ]
    },
    {
      path: '/TeacherMaterial',
      name: 'TeacherMaterial',
      component: TeacherMaterial,
      children: [
        {
          path: 'BuildMaterial',
          name: 'BuildMaterial',
          component: BuildMaterial
        },
        {
          path: 'ManageMaterial',
          name: 'ManageMaterial',
          component: ManageMaterial
        },
        {
          path: 'AllMaterial',
          name: 'AllMaterial',
          component: AllMaterial
        }
      ]
    },
    {
      path: '/StudentCommentAndDiscuss',
      name: 'StudentCommentAndDiscuss',
      component: StudentCommentAndDiscuss,
      children: [
        {
          path: 'StudentCourseComment',
          name: 'StudentCourseComment',
          component: StudentCourseComment
        },
        {
          path: 'CommentCourse',
          name: 'CommentCourse',
          component: CommentCourse
        }
      ]
    }
  ]
})
