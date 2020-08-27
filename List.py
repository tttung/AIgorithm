#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class solution(object):
    '反转链表'
    def ReverseLink(self, head):
        if not head:
            return
        cur = head
        pre = None
        next = None
        
        while(cur):
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
            #定义两个指针low和fast，low为慢指针，fast为快指针
            low,fast = head,head.next
            while fast and fast.next:
                if low==fast:
                    return True
                # low每次走一步，fast每次走两步
                low,fast = low.next, fast.next.next
            return False

    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

    '从尾到头打印链表'
    def reversePrint(self, head):
        return self.reversePrint(head.next) + [head.val] if head else []

    def reversePrint2(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

    '删除链表的节点'
    def deleteNode(self, head, val):
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head

    '链表中倒数第k个节点'
    def deleteKnode(self, k):
        pre,next = head,head
        for _ in range(k):
            next = next.next
        while nexr:
            pre,next = pre.next,next.next
        return pre

    '合并两个排序的链表'
    def mergeTwoList(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
    if l1.val <= l2.val:
        l1.next = mergeTwoList(l1.next, l2)
        return l1
    l2.next = mergeTwoList(l1, l2.next)
    return l2

    def mergeTwoLists(self, l1, l2):
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next

    '两个链表的第一个公共节点'
    def getIntersectionNode(self, headA, headB):
        node1, node2 = headA, headB
            
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1

if __name__ == '__main__':



