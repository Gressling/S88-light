<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="text" />

  <xsl:template match="/">
    <!-- List of Materials -->
    <xsl:text>List of Materials:&#10;</xsl:text>
    <xsl:apply-templates select="//material" />
  </xsl:template>
  
  <xsl:template match="material">
    <xsl:value-of select="concat(' - ', ., '&#10;')" />
  </xsl:template>
</xsl:stylesheet>
