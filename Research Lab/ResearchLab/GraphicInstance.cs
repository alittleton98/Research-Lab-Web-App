// Class representing the dash app sent to the iframe. Should contain the necessary graph/plot formatting
namespace ResearchLab
{
    public class GraphicInstance
    {
        string m_name;
        bool m_bIsRealTime;

        enum ChartType
        {
            SCATTER,
            LINE,
            BAR,
            PIE,
            BOX,
            HISTOGRAM,
            POLAR,
            NETWORK,
            HEATMAP,
            CANDLESTICK
        }

        struct ScatterPlot
        {
            string XAxis;
            string YAxis;
            string color; // indicates if the 
            string shape;
        }
    }
}
