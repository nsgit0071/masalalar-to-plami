class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_address = address.replace('.', '[.]')
        return defanged_address
        
