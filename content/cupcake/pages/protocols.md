Title: Protocols
Order: 03
Summary: Writing protocols with sections, steps and reagents, and importing them from protocols.io.
Screens: protocols, protocols/:id/edit

**Protocols** lists your protocols, those shared with you and public ones. Selecting one shows its description,
number of steps, ratings of complexity and duration, and where it came from.

![](shot:steps-cupcake/protocol-01-list)

## Creating a protocol

1. Choose **Create Protocol**, then **Create New** and enter the title and an optional description. **Enable for
   public view** lets others view and use it. **Import from protocols.io** imports a protocol from its protocols.io
   address instead, with its steps, sections and reagents.

    ![](shot:steps-cupcake/protocol-02-new)

2. The editor opens.

    ![](shot:steps-cupcake/protocol-03-editor)

3. Add a section and give it a title and a duration.

    ![](shot:steps-cupcake/protocol-04-section)

4. Select the section and **Add Step**: describe the step and optionally give its duration.

    ![](shot:steps-cupcake/protocol-05-step)

5. **Save Protocol**.

    ![](shot:steps-cupcake/protocol-06-written)

![](shot:gui-cupcake/cupcake-protocol-editor)

## Reagents in steps

A step can list the reagents it needs, with a quantity and unit. A **scalable** reagent's quantity is multiplied by
its scaling factor. In the step's description, `%ID.name%`, `%ID.quantity%`, `%ID.scaled_quantity%` and `%ID.unit%`
are replaced by the reagent's name, quantity, scaled quantity and unit, where `ID` is the step reagent's id; type a
space and `%` in the description to insert them.

## From a protocol

**Start Session** starts a session from the protocol; see [Sessions]({filename}sessions.md). **Export to
protocols.io** copies it to protocols.io; see [protocols.io]({filename}protocols-io.md).
