from string import Template

class View:
    def __init__(self, app_config):
        self.app_config = app_config
        self.html_header=Template(self.app_config.html_header)
        self.html_footer=Template(self.app_config.html_footer)
        self.section_header=Template(self.app_config.section_header)
        self.section_footer=Template(self.app_config.section_footer)
        self._html=''

    def get_html(self):
        return self._html

    def add_section(self, title, dataframe, note):
        self._html += self.section_header.substitute(qt_title=title)
        self._html += self.pandas_dataframe_to_html(dataframe)
        self._html += self.section_footer.substitute(qt_note=note)
    
    def set_html_header(self, subject):
        self._html=self.html_header.substitute(qt_title=subject)
    
    def set_html_footer(self, report_time):
        self._html += self.html_footer.substitute(qt_footer=report_time)

    def pandas_dataframe_to_html(self, dataframe):
        # html table
        html = '<table border="1" class="dataframe">\n'
        # header
        html += '  <thead>\n'
        # loop through columns
        # if column is a number, set align to right
        for col in dataframe.columns:
            if dataframe[col].dtype == 'float64' or dataframe[col].dtype == 'int64':
                html += '    <th align="right">{}</th>\n'.format(col)
            else:
                html += '    <th>{}</th>\n'.format(col)
        html += '  </thead>\n'
        # body
        html += '  <tbody>\n'
        # loop through rows
        # set color for even lines
        for index, row in dataframe.items():
            if index % 2 == 0:
                html += '    <tr style="background-color: #f2f2f2;">\n'
            else:
                html += '    <tr>\n'
            # index column
            html += '      <th>{}</th>\n'.format(index+1)
            # loop through columns
            # if column is a number, set align to right
            for col in dataframe.columns:
                html += '      <td>{}</td>\n'.format(row[col])
            html += '    </tr>\n'
        html += '  </tbody>\n'
        html += '</table>\n'
        return html
