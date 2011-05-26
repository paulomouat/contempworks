# coding: utf-8

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

composerFileTemplate = u"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
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
			{name}
			{descriptions}
		</td>
		<td width="25%">
			{length}
			{parts}
			{participants}
		</td>
		<td width="25%">
			{composed}
			{recorded}
			{release}
			{released}
		</td>
	</tr>"""
	
compositionNameRow = u"""
			<span class="composition_name">{name}</span>
			<br/>"""

compositionDescriptionRow = u"""
			<span class="composition_description">{description}</span>
			<br/>"""

compositionLengthRow = u"""
			<span class="composition_length">{length}</span>
			<br/>"""

compositionPartRow = u"""
			{number}. <i>{name}</i> {description} {composed} {length}
			<br/>"""

compositionParticipantRow = u"""
"""

compositionComposedRow = u"""
"""

compositionRecordedRow = u"""
"""

compositionReleaseRow = u"""
"""

compositionReleasedRow = u"""
"""