class StringChange:
    def change_case(str) -> str:
        res = [str[0].lower()]
        for c in str[1:]:
            if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                res.append('_')
                res.append(c.lower())
            else:
                res.append(c)

        return ''.join(res)