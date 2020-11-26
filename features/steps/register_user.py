#coding=utf-8
from behave import *
from features.lib.pages.register_page import RegisterPage

use_step_matcher('re')
'''
behave 提供3中step匹配模式
    'parse'
    'cfparse' 基于parse的扩展,  支持cardinality field syntax?
    're' 支持在step中定义正则表达式
'''

@When('I open the register website "([^"]*)"')
def step_register(context,url):
    RegisterPage(context).get_url(url)
    # context.driver.get(url)

@Then('I expect that the title is "([^"]*)"')
def step_register1(context,title_name):
    title = RegisterPage(context).get_title()
    # title = context.driver.title
    assert title_name in title
    
@When('I set with useremail "([^"]*)"')
def step_register2(context,useremail):
    RegisterPage(context).send_useremail(useremail)
    # context.driver.find_element_by_id('register_email').send_keys(useremail)
    
@When('I set with username "([^"]*)"')
def step_register3(context,username):
    RegisterPage(context).send_username(username)
    # context.driver.find_element_by_id('register_nickname').send_keys(username)
    
@When('I set with password "([^"]*)"')
def step_register4(context,password):
    RegisterPage(context).send_password(password)
    # context.driver.find_element_by_id('register_password').send_keys(password)

@When('I set with code "([^"]*)"')
def step_register5(context,code):
    RegisterPage(context).send_code(code)
    # context.driver.find_element_by_id('captcha_code').send_keys(code)
    
@When('I click with registerbutton')
def step_register6(context):
    RegisterPage(context).click_register_button()
    # context.driver.find_element_by_id('register-btn').click()
    
@Then('I expect that text "([^"]*)"')
def step_register7(context,code_text):
    text = RegisterPage(context).get_code_text()
    # text = context.driver.find_element_by_id('captcha_code-error').text
    assert code_text in text