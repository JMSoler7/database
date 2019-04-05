import App from './App.vue'
import { mount } from '@vue/test-utils'

describe('App.vue', () => {
  it('is a component', () => {
    const wrapper = mount(App)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
