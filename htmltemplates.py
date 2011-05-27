# coding: utf-8

composerListTemplate = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns:fo="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<style type="text/css">
			p
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
			}}
			th
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
				text-align: center;
			}}
			td
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
				text-align: top;
			}}
			span.bold
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
				font-weight: bold;
			}}
			span.name_initial
			{{					
				font-family: Verdana, Arial, Helvetica;
				font-size: 10pt;
				font-weight: bold;
			}}
		</style>
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

initialRow = u"""
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

composerListRow = u"""
		<tr>
			<td>
				<a href='{filename}'>{surname}, {name}</a> ({born}-{died})
			</td>
		</tr>"""

composerFileTemplate = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns:fo="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<style type="text/css">
			p
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
			}}
			th
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
				text-align: center;
			}}
			td
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
				text-align: top;
				border-bottom: #dddddd 1pt solid;
			}}
			span.bold
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
				font-weight: bold;
			}}
			span.composer_name
			{{					
				font-family: Verdana, Arial, Helvetica;
				font-size: 16pt;
				font-weight: bold;
				color: white;
			}}
			span.composer_dates
			{{					
				font-family: Verdana, Arial, Helvetica;
				font-size: 14pt;
				font-weight: bold;
				color: white;
			}}
			span.composition_name
			{{					
				font-family: Verdana, Arial, Helvetica;
				font-size: 10pt;
				font-weight: bold;
			}}
			span.composition_description
			{{					
				font-family: Verdana, Arial, Helvetica;
				font-size: 10pt;
			}}
			span.composition_length
			{{					
				font-family: Verdana, Arial, Helvetica;
				font-size: 10pt;
			}}
			span.player
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
			}}
			span.instrument
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
				font-style: italic;
			}}
			span.part
			{{
				font-family: Verdana, Arial, Helvetica;
				font-size: 8pt;
			}}				
		</style>
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
		
composerTitleRow = u"""
	<tr>
		<td colspan="3" bgcolor="#888888">
			<span class="composer_name">{name} {surname}</span>
			<span class="composer_dates"> ({born}-{died})</span>
		</td>
	</tr>"""

compositionRow = u"""
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
	
compositionNameRow = u"""
			<span class="composition_name">{name}</span>"""

compositionDescriptionRow = u"""
			<span class="composition_description">{description}</span>
			<br/>"""

compositionLengthRow = u"""
			<span class="composition_length">{length}</span>"""

compositionPartRow = u"""
			{number}. <i>{name}</i> {description} {composed} {length}
			<br/>"""

compositionInstrumentRow = u"""
			{players}<span class="instrument">{name}</span>"""

compositionConductorRow = u"""
			Dir.: {name}"""

compositionParticipantRow = u"""{participant}<br/>"""

compositionComposedRow = u"""({composed})"""
