#!/usr/bin/env python
# -*- coding: utf-8 -*-

class list(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    '反转链表'
    def ReverseLink(self, head):
        if not head:
            return
        cur = head
        pre = None
        next = None
        
        while(root):
            next = cur.next
            cur.next = pre
            
            pre = cur
            cur = next
        return pre

    def reverseLink(self, head):
        if not head or not head.next:
            return head
        newHead = reverseLink(head.next)
        head.next.next = head
        head.next = None
        return newHead

    '环形链表'
    def hasCycle(self, head):
            if not (head and head.next):
                return False
            #定义两个指针i和j，i为慢指针，j为快指针
            i,j = head,head.next
            while j and j.next:
                if i==j:
                    return True
                        # i每次走一步，j每次走两步
                i,j = i.next, j.next.next
            return False


