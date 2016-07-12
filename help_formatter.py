import argparse

"""
A formatter class remove duplicated metavar

From: http://stackoverflow.com/a/16969505/3962533
"""
class SingleMetavarHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar

        else:
            parts = []

            # if the Optional doesn't take a value, format is:
            #    -s, --long
            if action.nargs == 0:
                parts.extend(action.option_strings)

            # if the Optional takes a value, format is:
            #    -s ARGS, --long ARGS
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)

                ## THIS IS THE PART REPLACED
                #~ for option_string in action.option_strings:
                    #~ parts.append('%s %s' % (option_string, args_string)) ### this is change
                ## /SECTION REPLACED

                ## NEW CODE:
                parts.extend(action.option_strings)
                parts[-1] += ' %s' % args_string
                ## /NEW CODE
            return ', '.join(parts)
