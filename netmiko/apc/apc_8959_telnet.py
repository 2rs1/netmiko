from netmiko.apc.apc_base import APCBase, APC_PROMPT


class APC8959(APCBase):
    def telnet_login(self,
                     pri_prompt_terminator=APC_PROMPT,
                     alt_prompt_terminator=APC_PROMPT,
                     username_pattern=r"User Name :",
                     pwd_pattern=r"Password  :",
                     *args,
                     **kwargs):
        return super(APC8959, self).telnet_login(
            pri_prompt_terminator=pri_prompt_terminator,
            alt_prompt_terminator=alt_prompt_terminator,
            username_pattern=username_pattern,
            pwd_pattern=pwd_pattern,
            *args, **kwargs)
