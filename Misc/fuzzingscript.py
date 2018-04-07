# This pulls in the canape library namespaces
import CANAPE.Nodes
import CANAPE.DataFrames

# Simple pipeline node
class PipelineNode(CANAPE.Nodes.BaseDynamicPipelineNode):

    # Called when a new frame has arrived
    def OnInput(self, frame):
        cmd = self.Graph.IncrementGlobalCounter("CurrentCommand", 1)
        
        self.LogInfo("Current Command {0}", cmd)
        
        # XPATH Method
        #cmdval = frame.SelectSingleNode("/Command")
        #cmdval.Value = cmd
        
        # Dynamic Method
        frame.DynamicRoot.Command.Value = cmd
        
        self.WriteOutput(frame)