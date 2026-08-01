class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for i in emails:
            locname = i.split("@")
            local = locname[0].split("+")[0]
            local = local.replace(".", "")
            unique_emails.add(local+ "@" + locname[1])
        return len(unique_emails)