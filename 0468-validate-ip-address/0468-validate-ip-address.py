class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            subs = queryIP.split('.')
            if len(subs) != 4:
                return "Neither"
            for n in subs:
                # must be digits only
                if not n.isdigit():
                    return "Neither"
                # no leading zeros allowed unless single digit
                if (n[0] == '0' and len(n) > 1):
                    return "Neither"
                # numeric range check
                if not (0 <= int(n) <= 255):
                    return "Neither"
            return "IPv4"

        elif queryIP.count(':') == 7:
            subs = queryIP.split(':')
            if len(subs) != 8:
                return "Neither"
            hex_digits = "0123456789abcdefABCDEF"
            for n in subs:
                # each block 1–4 chars
                if len(n) == 0 or len(n) > 4:
                    return "Neither"
                # hex validation
                for ch in n:
                    if ch not in hex_digits:
                        return "Neither"
            return "IPv6"

        return "Neither"


