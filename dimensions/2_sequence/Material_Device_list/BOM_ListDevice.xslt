<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="text" />

  <xsl:template match="/">
    <!-- List of materials -->
    <xsl:text>List of Materials:&#10;</xsl:text>
    <xsl:apply-templates select="//material" />
    
    <!-- List of devices -->
    <xsl:text>&#10;List of Devices:&#10;</xsl:text>
    <xsl:apply-templates select="//device" />
  </xsl:template>
  
  <xsl:template match="material">
    <xsl:value-of select="concat(' - ', ., '&#10;')" />
  </xsl:template>
  
  <xsl:template match="device">
    <xsl:value-of select="concat(' - ', ., '&#10;')" />
  </xsl:template>
</xsl:stylesheet>
