<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/xhtml">
	<xsl:output method="html" encoding="iso-8859-1" doctype-public="-//W3C//DTD XHTML 1.0 Transitional//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"/>
	<xsl:template match="/">
		<html>
			<head>
				<style type="text/css">
			   p
				{
					font-family: Verdana, Arial, Helvetica;
					font-size: 8pt;
				}
			   th
				{
					font-family: Verdana, Arial, Helvetica;
					font-size: 8pt;
					text-align: center;
				}
				td
				{
					font-family: Verdana, Arial, Helvetica;
					font-size: 8pt;
					text-align: top;
					border-bottom: #dddddd 1pt solid;
				}
				span.bold
				{
					font-family: Verdana, Arial, Helvetica;
					font-size: 8pt;
					font-weight: bold;
				}
				span.composer_name
				{					
					font-family: Verdana, Arial, Helvetica;
					font-size: 16pt;
					font-weight: bold;
					color: white;
				}
				span.composer_dates
				{					
					font-family: Verdana, Arial, Helvetica;
					font-size: 14pt;
					font-weight: bold;
					color: white;
				}
				span.composition_name
				{					
					font-family: Verdana, Arial, Helvetica;
					font-size: 10pt;
					font-weight: bold;
				}
				span.composition_description
				{					
					font-family: Verdana, Arial, Helvetica;
					font-size: 10pt;
				}
				span.composition_length
				{					
					font-family: Verdana, Arial, Helvetica;
					font-size: 10pt;
				}
				span.player
				{
					font-family: Verdana, Arial, Helvetica;
					font-size: 8pt;
				}
				span.instrument
				{
					font-family: Verdana, Arial, Helvetica;
					font-size: 8pt;
					font-style: italic;
				}
				span.part
				{
					font-family: Verdana, Arial, Helvetica;
					font-size: 8pt;
				}				
			</style>
			</head>
			<body>
				<p>
					<xsl:apply-templates select="list"/>
				</p>
			</body>
		</html>
	</xsl:template>
	<xsl:template match="list">
		<table>
			<xsl:apply-templates select="composer">
				<xsl:sort order="ascending" select="@surname"/>
				<xsl:sort order="ascending" select="@name"/>
			</xsl:apply-templates>
		</table>
	</xsl:template>
	<xsl:template match="composer">
		<tr>
			<td colspan="3" bgcolor="#888888">
				<span class="composer_name">
					<xsl:value-of select="@name"/>
					<xsl:text> </xsl:text>
					<xsl:value-of select="@surname"/>
				</span>
				<span class="composer_dates"> (<xsl:value-of select="@born"/>-<xsl:if test="@died &gt; 0">
						<xsl:value-of select="@died"/>
					</xsl:if>)</span>
			</td>
		</tr>
		<xsl:apply-templates select="composition">
			<xsl:sort order="ascending" select="composed/@start"/>
			<xsl:sort order="ascending" select="composed/@end"/>
		</xsl:apply-templates>
	</xsl:template>
	<xsl:template match="composition">
		<tr valign="top">
			<td width="25%">
				<span class="composition_name">
					<xsl:value-of select="name"/>
				</span>
				<br/>
				<xsl:apply-templates select="description"/>
			</td>
			<td width="25%">
				<xsl:apply-templates select="length"/>
				<xsl:apply-templates select="part"/>
				<xsl:apply-templates select="instrument"/>
				<xsl:apply-templates select="player"/>
				<xsl:apply-templates select="conductor"/>
			</td>
			<td width="25%">
				<xsl:apply-templates select="composed"/><br/>
				<xsl:apply-templates select="recorded"/>
				<xsl:apply-templates select="release"/>
				<xsl:apply-templates select="released"/>
			</td>
		</tr>
	</xsl:template>
	<xsl:template match="description">
		<xsl:if test="not(description=&quot;&quot;)">
			<span class="composition_description">
				<xsl:value-of select="."/>
			</span>
			<br/>
		</xsl:if>
	</xsl:template>
	<xsl:template match="length">
		<xsl:if test="not(length=&quot;&quot;)">
			<span class="composition_length">
				<xsl:value-of select="."/>
			</span>
			<br/>
		</xsl:if>
	</xsl:template>
	<xsl:template match="part">
		<xsl:value-of select="number"/>
		<xsl:text>. </xsl:text>
		<i>
			<xsl:value-of select="name"/>
		</i>
		<xsl:text> </xsl:text>
		<xsl:apply-templates select="composed"/>
		<xsl:value-of select="length"/>
		<br/>
	</xsl:template>
	<xsl:template match="instrument">
		<xsl:for-each select="player">
			<xsl:value-of select="@name"/>
			<xsl:if test="not(position()=last())">
				<xsl:text>, </xsl:text>
			</xsl:if>
		</xsl:for-each>
		<xsl:text>, </xsl:text>
		<span class="instrument">
			<xsl:value-of select="@name"/>
		</span>
		<br/>
	</xsl:template>
	<xsl:template match="player">
		<xsl:value-of select="@name"/>
		<br/>
	</xsl:template>
	<xsl:template match="conductor">
		<xsl:if test="not(conductor=&quot;&quot;)">
			<xsl:text>Dir.: </xsl:text>
			<xsl:value-of select="."/>
			<br/>
		</xsl:if>
	</xsl:template>
	<xsl:template match="composed">
	(<xsl:value-of select="@start"/>
		<xsl:if test="@end &gt; 0">-<xsl:value-of select="@end"/>
		</xsl:if>)
	</xsl:template>
	<xsl:template match="recorded">
	Rec.: <xsl:value-of select="@start"/>
		<xsl:if test="@end &gt; 0">-<xsl:value-of select="@end"/>
		</xsl:if>
		<br/>
	</xsl:template>
	<xsl:template match="release">
		<xsl:if test="not(release=&quot;&quot;)">
			<xsl:value-of select="."/>
		</xsl:if>
	</xsl:template>
	<xsl:template match="released">
		<xsl:if test="not(released=&quot;&quot;)"> (<xsl:value-of select="."/>)</xsl:if>
	</xsl:template>
</xsl:stylesheet>
