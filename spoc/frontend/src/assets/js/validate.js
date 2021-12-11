export function validatePassword (rule, value, callback) {
  const passwordRegex = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$/
  if (value === '' || value === undefined || value === null) {
    callback()
  } else {
    if ((!passwordRegex.test(value)) && value !== '') {
      callback(new Error('请输入6-16位由数字和字母构成的密码!'))
    } else {
      callback()
    }
  }
}

export function validateStudentUserName (rule, value, callback) {
  const userName = /[0-9]{6}/
  if (value === '' || value === undefined || value === null) {
    callback()
  } else {
    if ((!userName.test(value)) && value !== '') {
      callback(new Error('请输入6位由数字构成的学号!'))
    } else {
      callback()
    }
  }
}
