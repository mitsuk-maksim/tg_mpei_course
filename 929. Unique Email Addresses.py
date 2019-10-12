# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        count = 0
        for email in emails:
            local = email.split("@")[0].split('+')[0].replace('.','')
            domain = email.split('@')[1]
            address = local + '@' + domain
            if address not in res:
                res.append(address)
                count += 1
        return count
        
