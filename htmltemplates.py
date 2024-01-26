# coding: utf-8

composerListTemplate = """<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="list.css"/>
	</head>
	<body>
		<a name="top"></a>
		<table>
			<tr>
				<td colspan="2">
					Alphabetical list of composers
				</td>
			</tr>
			<tr>
				<td colspan="2">
					<a href="#A">A</a>
					<a href="#B">B</a>
					<a href="#C">C</a>
					<a href="#D">D</a>
					<a href="#E">E</a>
					<a href="#F">F</a>
					<a href="#G">G</a>
					<a href="#H">H</a>
					<a href="#I">I</a>
					<a href="#J">J</a>
					<a href="#K">K</a>
					<a href="#L">L</a>
					<a href="#M">M</a>
					<a href="#N">N</a>
					<a href="#O">O</a>
					<a href="#P">P</a>
					<a href="#Q">Q</a>
					<a href="#R">R</a>
					<a href="#S">S</a>
					<a href="#T">T</a>
					<a href="#U">U</a>
					<a href="#V">V</a>
					<a href="#W">W</a>
					<a href="#X">X</a>
					<a href="#Y">Y</a>
					<a href="#Z">Z</a>
				</td>
			</tr>
			{composerList}
		</table>
	</body>
</html>"""

initialRow = """
		<tr>
			<td>
				<span class='name_initial'>
					<a name='{initial}'>{initial}</a>
				</span>
			</td>
			<td>
				<span>
					<a href='#top'>back to top</a>
				</span>
			</td>
		</tr>"""

composerListRow = """
		<tr>
			<td>
				<a href='{filename}'>{surname}, {name}</a> ({born}-{died})
			</td>
		</tr>"""

composerFileTemplate = """<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="composer.css"/>
	</head>
	<body>
		<p>
			<table>
				{composerTitle}
				{compositions}
			</table>
		</p>
	</body>
</html>"""
		
composerTitleRow = """
	<tr>
		<td colspan="3" bgcolor="#888888">
			<span class="composer_name">{name} {surname}</span>
			<span class="composer_dates"> ({born}-{died})</span>
		</td>
	</tr>"""

compositionRow = """
	<tr valign="top">
		<td width="25%">
			{name}<br/>
			{descriptions}
		</td>
		<td width="25%">
			{length}<br/>
			{parts}
			{participants}
		</td>
		<td width="25%">
			{composed}<br/>
			Rec.: {recorded}<br/>
			{release} ({released})
		</td>
	</tr>"""
	
compositionNameRow = """
			<span class="composition_name">{name}</span>"""

compositionDescriptionRow = """
			<span class="composition_description">{description}</span>
			<br/>"""

compositionLengthRow = """
			<span class="composition_length">{length}</span>"""

compositionPartRow = """
			{number}. <i>{name}</i> {description} {composed} {length}            
			<br/>{participants}"""

partParticipantRow = """{participant}"""

compositionInstrumentRow = """
			{players}<span class="instrument">{name}</span>"""

compositionConductorRow = """
			Dir.: {name}"""

compositionParticipantRow = """{participant}<br/>"""

compositionComposedRow = """({composed})"""
