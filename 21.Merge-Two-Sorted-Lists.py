"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:

        #      ____
        #     |DD|_\___
        #     |  dummy |
        #     '-O----O-'
        #        ^
        #       tail
        dummy = ListNode()
        tail = dummy

        #   list1:  .---.   .---.
        #           | 1 |===| 3 |===> None
        #           'o-o'   'o-o'
        #
        #   list2:  .---.   .---.
        #           | 2 |===| 4 |===> None
        #           'o-o'   'o-o'
        while list1 and list2:
            #      [ 1 ]  vs  [ 2 ]
            #        \          /
            #         \  (o_o) /
            #          smaller?
            if list1.val <= list2.val:
                #    ____
                #   |DD|_\___   .---.
                #   |  dummy |==| 1 |  <-- hook!
                #   '-O----O-'  'o-o'
                tail.next = list1
                list1 = list1.next

            else:
                #    ____
                #   |DD|_\___   .---.
                #   |  dummy |==| 2 |  <-- hook!
                #   '-O----O-'  'o-o'
                tail.next = list2
                list2 = list2.next

            #    ____
            #   |DD|_\___   .---.
            #   |  dummy |==| 1 |
            #   '-O----O-'  'o-o'
            #                 ^
            #              \(^o^)/  tail hops on
            tail = tail.next

        #    ____
        #   |DD|_\___   .---.   .---.   .---.        .---.
        #   |  dummy |==| 1 |===| 2 |===| 3 |  <===  | 4 |===> None
        #   '-O----O-'  'o-o'   'o-o'   'o-o'        'o-o'
        #                                 ^         leftovers
        #                                tail
        tail.next = list1 if list1 else list2

        #    ____
        #   |DD|_\___  ✂  .---.   .---.   .---.   .---.
        #   |  dummy |    | 1 |===| 2 |===| 3 |===| 4 |===> None
        #   '-O----O-'    'o-o'   'o-o'   'o-o'   'o-o'
        #                   ^
        #               dummy.next
        return dummy.next


# --
