from netmiko import BaseConnection


APC_PROMPT = 'apc>'


class APCBase(BaseConnection):
    def check_enable_mode(self, *args, **kwargs):
        """Not in use"""
        return

    def enable(self, *args, **kwargs):
        """Not in use"""
        return

    def exit_enable_mode(self, *args, **kwargs):
        """Not in use"""
        return

    def check_config_mode(self, *args, **kwargs):
        """Not in use"""
        return

    def config_mode(self, *args, **kwargs):
        """Not in use"""
        return

    def exit_config_mode(self, *args, **kwargs):
        """Not in use"""
        return

    def session_preparation(self):
        self._test_channel_read()
        self.set_base_prompt()

    def cleanup(self):
        """Gracefully exit the SSH session."""
        self.write_channel('quit\n')

    def run_command(self, command, outlet, delay=0):
        if delay > 0:
            cmd = 'ol{dly}{command} {outlet}'
        else:
            cmd = 'ol{dly}{command} {outlet} {delay}'
        return self.send_command(cmd.format(dly='Dly' if delay else '',
                                            command=command,
                                            outlet=outlet,
                                            delay=delay))

    def power_cycle(self, *args, **kwargs):
        return self.run_command('Reboot', *args, **kwargs)

    def power_off(self, *args, **kwargs):
        return self.run_command('Off', *args, **kwargs)

    def power_on(self, *args, **kwargs):
        return self.run_command('On', *args, **kwargs)
