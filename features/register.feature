#coding=utf-8
Feature: Register User
    
    As a developer
    This is my first bdd project
    Scenario: open register website
        When I open the register website "http://www.5itest.cn/register"
        Then I expect that the title is "注册"

    Scenario: input username
        When I set with useremail "GGW@qq.com"
        And I set with username "GGW"
        And I set with password "GGW01"
        And I set with code "tets"
        And I click with registerbutton
        Then I expect that text "验证码错误"
        