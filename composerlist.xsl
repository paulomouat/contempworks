<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" encoding="iso-8859-1"/>
	<xsl:template match="/">
		<xsl:apply-templates select="list"/>
	</xsl:template>
	<xsl:template match="list">
			<tr>
				<td><span class="name_initial"><a name="{$initial}"><xsl:value-of select="$initial"/></a></span></td>
				<td><span><a href="#top">back to top</a></span></td>
			</tr>
			<xsl:apply-templates select="composer">
				<xsl:sort order="ascending" select="@surname"/>
				<xsl:sort order="ascending" select="@name"/>
			</xsl:apply-templates>
	</xsl:template>
	<xsl:template match="composer">
		<tr>
			<td>
				<xsl:variable name="escaped-name">
					<xsl:call-template name="escape-name">
						<xsl:with-param name="name" select="@name"/>
						<xsl:with-param name="surname" select="@surname"/>
					</xsl:call-template>
				</xsl:variable>
				<xsl:variable name="href">
					<xsl:value-of select="$escaped-name"/><xsl:text>.html</xsl:text>
				</xsl:variable>
				<a><xsl:attribute name="href"><xsl:value-of select="$href"/></xsl:attribute><xsl:value-of select="@surname"/>,<xsl:text> </xsl:text><xsl:value-of select="@name"/></a><xsl:text> </xsl:text>(<xsl:value-of select="@born"/>-<xsl:if test="@died &gt; 0"><xsl:value-of select="@died"/></xsl:if>)
				<xsl:document href="generated/{$href}" method="html" encoding="iso-8859-1">
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
								<table>
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
								</table>
							</p>
						</body>
					</html>
				</xsl:document>
			</td>
			<td></td>
		</tr>
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
		<xsl:value-of select="description"/>
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
	
	<xsl:template name="escape-name">
		<xsl:param name="name"/>
		<xsl:param name="surname"/>
		<xsl:variable name="concatenated">
			<xsl:value-of select="concat($name,$surname)"/>
		</xsl:variable>
		<xsl:variable name="lowercased">
			<xsl:call-template name="lower-case">
				<xsl:with-param name="word" select="$concatenated"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:variable name="escaped">		
			<xsl:call-template name="escape-word">
				<xsl:with-param name="word" select="$lowercased"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:value-of select="$escaped"/>
	</xsl:template>

	<xsl:template name="lower-case">
		<xsl:param name="word"/>
		<xsl:value-of select="translate($word,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
	</xsl:template>

	<xsl:template name="string-replace-all">
	  <xsl:param name="text"/>
	  <xsl:param name="replace"/>
	  <xsl:param name="by"/>
	  <xsl:choose>
	    <xsl:when test="contains($text,$replace)">
	      <xsl:value-of select="substring-before($text,$replace)"/>
	      <xsl:value-of select="$by"/>
	      <xsl:call-template name="string-replace-all">
	        <xsl:with-param name="text" select="substring-after($text,$replace)"/>
	        <xsl:with-param name="replace" select="$replace"/>
	        <xsl:with-param name="by" select="$by"/>
	      </xsl:call-template>
	    </xsl:when>
	    <xsl:otherwise>
	      <xsl:value-of select="$text"/>
	    </xsl:otherwise>
	  </xsl:choose>
	</xsl:template>
	
	<xsl:template name="escape-word">
		<xsl:param name="word"/>
		<xsl:variable name="a-raw" select="'&#192;&#193;&#194;&#195;&#196;&#197;&#198;&#224;&#225;&#226;&#227;&#228;&#229;&#230;'" />
		<xsl:variable name="a-new" select="'aaaaaaaaaaaaaa'" />
		<xsl:variable name="a-escaped" select="translate($word,$a-raw,$a-new)"/>
		<xsl:variable name="c-raw" select="'&#199;&#231;'" />
		<xsl:variable name="c-new" select="'cc'" />
		<xsl:variable name="c-escaped" select="translate($a-escaped,$c-raw,$c-new)"/>
		<xsl:variable name="e-raw" select="'&#200;&#201;&#202;&#203;&#232;&#233;&#234;&#235;&#208;&#240;'" />
		<xsl:variable name="e-new" select="'eeeeeeeeee'" />
		<xsl:variable name="e-escaped" select="translate($c-escaped,$e-raw,$e-new)"/>
		<xsl:variable name="i-raw" select="'&#204;&#205;&#206;&#207;&#236;&#237;&#238;&#239;'" />
		<xsl:variable name="i-new" select="'iiiiiiii'" />
		<xsl:variable name="i-escaped" select="translate($e-escaped,$i-raw,$i-new)"/>
		<xsl:variable name="n-raw" select="'&#209;&#241;'" />
		<xsl:variable name="n-new" select="'nn'" />
		<xsl:variable name="n-escaped" select="translate($i-escaped,$n-raw,$n-new)"/>
		<xsl:variable name="o-raw" select="'&#210;&#211;&#212;&#213;&#214;&#216;&#242;&#243;&#244;&#245;&#246;&#248;'" />
		<xsl:variable name="o-new" select="'oooooooooooo'" />
		<xsl:variable name="o-escaped" select="translate($n-escaped,$o-raw,$o-new)"/>
		<xsl:variable name="u-raw" select="'&#217;&#218;&#219;&#220;&#249;&#250;&#251;&#252;'" />
		<xsl:variable name="u-new" select="'uuuuuuuu'" />
		<xsl:variable name="u-escaped" select="translate($o-escaped,$u-raw,$u-new)"/>
		<xsl:variable name="y-raw" select="'&#221;&#253;&#255;'" />
		<xsl:variable name="y-new" select="'yyy'" />
		<xsl:variable name="y-escaped" select="translate($u-escaped,$y-raw,$y-new)"/>
		<xsl:variable name="misc-raw" select="' '" />
		<xsl:variable name="misc-new" select="'-'" />
		<xsl:variable name="misc-escaped" select="translate($y-escaped,$misc-raw,$misc-new)"/>
		<xsl:variable name="sz-raw" select="'&#223;'" />
		<xsl:variable name="sz-new" select="'ss'" />
		<xsl:call-template name="string-replace-all">
			<xsl:with-param name="text" select="$misc-escaped"/>
			<xsl:with-param name="replace" select="$sz-raw"/>
			<xsl:with-param name="by" select="$sz-new"/>
		</xsl:call-template>
	</xsl:template>
	
</xsl:stylesheet>
